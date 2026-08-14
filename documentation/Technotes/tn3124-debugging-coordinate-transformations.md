# TN3124: Debugging coordinate space issues

**Framework**: Technotes

Learn techniques to help debug any coordinate space issue.

#### Overview

Working with coordinate spaces is an essential part of developing any graphics-based app. Issues related to assumptions or misinterpretations of a coordinate space are difficult to debug, or even identify. Read this technote to discover effective strategies for diagnosing and debugging coordinate space issues.

#### Recognize the Issue

Coordinate space issues can be difficult to recognize, but there are some common symptoms that can help to diagnose them:

- Unexpected or absent visual appearance
- Incorrect behavior of user-interaction
- Wrong values after a coordinate conversion

Assume that there is a coordinate space issue that needs to be debugged if you notice any of these symptoms in your app.

#### Identify the Coordinate Spaces Involved

Coordinate spaces are ubiquitous in the graphics world. Even simple apps will involve many different coordinate spaces. Identifying the coordinate spaces involved is essential to debugging issues with them.

Consider the following SwiftUI snippet:

```swift
struct ContentView: View {
    
    @State private var uiImage = UIImage()
    
    var body: some View {
        VStack {
            Image(uiImage: uiImage)
            Button("Hello") {
                print("World.")
            }
        }
    }
}
```

This snippet, while simple, actually involves five different coordinate spaces:

1. The local coordinate space of the `VStack`.
2. The local coordinate space of the `Image`.
3. The local coordinate space of the `Button`.
4. The local coordinate space of the `UIImage`.
5. The global coordinate space of `SwiftUI`.

#### Create a Focused Sample

Coordinate space issues are often very complex and difficult to reason about. Creating a focused sample project that visualizes origins, logs transforms and bounding boxes, and utilizes known points is an extremely effective tool for debugging coordinate space issues.

#### Visualize the Origin

The best first step towards understanding a coordinate space is to visualize its origin.

> ⚠️ **Warning**: Do not rely on textual descriptions of a coordinate space, they are easy to misinterpret.

Projects targeting visionOS can use [`Diagnosing issues in the appearance of a running app`](https://developer.apple.com/documentation/xcode/diagnosing-issues-in-the-appearance-of-your-running-app). In other contexts, the exact code to visualize the origin will differ depending on the framework involved.

Some frameworks offer built-in ways to visualize certain origins. For example, `ARView` and `ARSCNView` both have API to visualize the world origin for debugging:

```swift
view.debugOptions.insert(.showWorldOrigin)
```

`ARView` has additional API to visualize anchor origins:

```swift
view.debugOptions.insert(.showAnchorOrigins)
```

Other frameworks may not have origin visualization API to aid in debugging, but it is always possible to write visualization code for any coordinate space. For example, this snippet visualizes the origin of any SwiftUI `View`:

```swift
import SwiftUI

extension View {
    /// Visualizes the origin of any View for debugging purposes.
    /// The x-axis is red, the y-axis is green.
    public func showOrigin() -> some View {
        modifier(CoordinateAxes())
    }
}

private struct CoordinateAxes: ViewModifier {
        
    func body(content: Content) -> some View {
        content.overlay {
            
            GeometryReader { geometry in
                
                let size = geometry.size
                
                let smallestDim = min(size.width, size.height)
                
                // Set length to be at least 20 points.
                let length = max(smallestDim * 0.2, 20)
                let thickness = length / 7
                
                // X-axis.
                Color.red
                    .frame(width: length, height: thickness)
                    .position(.init(x: length / 2, y: thickness / 2))
                
                // Y-axis.
                Color.green
                    .frame(width: thickness, height: length)
                    .position(.init(x: thickness / 2, y: length / 2))
            }
        }
    }
}
```

Visualizing an origin could be all that is necessary to realize where the error is.

#### Understand Input Expectations

Sometimes an API requires inputs that are already in a particular coordinate space. Otherwise its output is invalid.

Consider the `UIView` method, [`hitTest(_:with:)`](https://developer.apple.com/documentation/uikit/uiview/hittest(_:with:)). This method accepts a `CGPoint` as input, and uses it to perform a hit-test on the view. The problem here is that its results aren’t valid for *any* `CGPoint`, you must provide a `CGPoint` in the view’s local coordinate space to get a valid result.

When you have results that don’t make sense, it is a good idea to evaluate the APIs you are using to produce the results, and verify that you have provided inputs to them in the coordinate spaces they are expecting.

#### Use Known Points

Using known points is an effective graphics debugging technique.

Consider an app that runs a `VNDetectRectanglesRequest` on a `CMSampleBuffer` stream, displays the stream in an `AVCaptureVideoPreviewLayer`, and then attempts to draw the detected rectangles on top of the preview layer in an overlay `CALayer`, but the drawing doesn’t appear as expected. After gaining an understanding of each coordinate space involved in the drawing process (the `AVCaptureVideoPreviewLayer`, the overlay `CALayer`, and the `VNRectangleObservation`) by visualizing their origins, it can be helpful to draw a known point, instead of trying to debug this on the fly with a dynamic video stream. In this specific example, you might use `CGRect(x: 0, y: 0, width: 0.25, height: 0.25)` as the input, a rectangle that you would expect to cover one quarter of the preview image when drawn correctly.

Being consistent with the data you feed through a coordinate conversion pipeline allows you to clearly see the effects of any changes you make when debugging.

#### Log Transforms and Bounding Boxes

Logging the transform and bounding box of a visual element is a simple but effective debugging technique.

Consider a scenario where your app is inserting a 3D model into a scene, but you don’t see the 3D model where you expected to see it. By logging the transform and bounding box of the model, you discover that the scale and the bounding box of the model is very large. This is a very good indication that the model is so large that the current viewpoint of the 3D scene is *inside* of the model. You remedy the situation by setting the model’s scale factor to a smaller value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3124-debugging-coordinate-transformations)*