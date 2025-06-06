# init(consumer:mediaBox:_:)

**Framework**: Core Graphics  
**Kind**: init

Creates a PDF graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(consumer: CGDataConsumer, mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)
```

#### Return Value

A new PDF context, or `NULL` if the context cannot be created. In Objective-C, you’re responsible for releasing this object using [`CGContextRelease`](cgcontextrelease.md).

#### Discussion

This function creates a PDF drawing environment to your specifications. When you draw into the new context, Core Graphics renders your drawing as a sequence of PDF drawing commands that are passed to the data consumer object.

## Parameters

- `consumer`: The data consumer to receive the PDF output data.
- `mediaBox`: A pointer to a rectangle that defines the size and location of the PDF page, or  . The origin of the rectangle should typically be  . Core Graphics uses this rectangle as the default bounds of the page’s media box. If you pass  , Core Graphics uses a default page size of 8.5 by 11 inches (612 by 792 points).
- `auxiliaryInfo`: A dictionary that specifies any additional information to be used by the PDF context when generating the PDF file, or  . The dictionary is retained by the new context, so on return you may safely release it. See   for keys you can include in the dictionary.

## See Also

- [init?(CFURL, mediaBox: UnsafePointer<CGRect>?, CFDictionary?)](cgcontext/init(_:mediabox:_:).md)
  Creates a URL-based PDF graphics context.
- [Auxiliary Dictionary Keys](auxiliary-dictionary-keys.md)
  Keys for the auxiliary info dictionary you specify when creating a PDF context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/init(consumer:mediabox:_:))*