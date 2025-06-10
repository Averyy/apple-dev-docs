# withBNNSTensor(_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with a pointer to a BNNS tensor that shares memory with the pixel buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func withBNNSTensor<R>(_ body: (BNNSTensor) throws -> R) rethrows -> R
```

#### Discussion

Use this function to pass image data to a `BNNSGraph`. For example, the following code creates a graph that calculates the mean value of an image and apply a threshold based on the mean.

```None
let context = try BNNSGraph.makeContext {
   builder in

   let src = builder.argument(name: "source",
                              dataType: Float16.self,
                              shape: [<height, width, channels count>])

   let mean = src.mean(axes: [0, 1], keepDimensions: false)

   let thresholded = src .> mean

   let result = thresholded.cast(to: Float16.self)

   return [result]
}
```

Use `withBNNSTensor()` to pass source and destination pixel buffers to the context:

```None
let source = vImage.PixelBuffer<vImage.Planar16F>(...)
let destination = vImage.PixelBuffer<vImage.Planar16F>(...)
source.withBNNSTensor { src in
    destination.withBNNSTensor { dst in

        var args = [dst, src]

        try! context.executeFunction(arguments: &args)
    }
}
```

On return, `destination` contains the thresholded image data.

Note that the tensor that this function creates has the shape `height, width, channels count`.  If you appy a slice operation to a pixel buffer back tensor, the first dimension is the height and the second dimension is the width.

For example, given the following code:

```None
   let sourcePixels: [Float] = [
       001, 002, 003, 004,     005, 006, 007, 008,     009, 010, 011, 012,
       013, 014, 015, 016,     017, 018, 019, 020,     021, 022, 023, 024,
       025, 026, 027, 028,     029, 030, 031, 032,     033, 034, 035, 036,
       037, 038, 039, 040,     041, 042, 043, 044,     045, 046, 047, 048,
       049, 050, 051, 052,     053, 054, 055, 056,     057, 058, 059, 060
   ]

   let source = vImage.PixelBuffer(pixelValues: sourcePixels,
                                   size: .init(width: 3, height: 5),
                                   pixelFormat: vImage.InterleavedFx4.self)

   let destination = vImage.PixelBuffer(size: .init(width: 2, height: 3),
                                        pixelFormat: vImage.InterleavedFx4.self)

   let context = try BNNSGraph.makeContext {
       builder in

       let src = builder.argument(name: "source",
                                  dataType: Float.self,
                                  shape: [ -1, -1, -1])

       let result = src[ 0...2,    // rows 0, 1, 2
                         1...2,    // cols 1, 2
                         0...3 ]   // channels 0, 1, 2, 3

       return [result]
   }

   source.withBNNSTensor { src in
       destination.withBNNSTensor { dst in

           var args = [dst, src]
           try! context.executeFunction(arguments: &args)
       }
   }
```

The slice selects rows 0, 1, and 2 and columns 1 and 2. On return, `destination` contains the following values:

```None
       [
           005, 006, 007, 008,     009, 010, 011, 012,
           017, 018, 019, 020,     021, 022, 023, 024,
           029, 030, 031, 032,     033, 034, 035, 036,
       ]
```

- Returns The return value, if any, of the body closure parameter.

## Parameters

- `body`: A closure with a   parameter


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withbnnstensor(_:))*