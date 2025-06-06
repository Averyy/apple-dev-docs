# init(_:mediaBox:_:)

**Framework**: Core Graphics  
**Kind**: init

Creates a URL-based PDF graphics context.

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
init?(_ url: CFURL, mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)
```

#### Return Value

A new PDF context, or `NULL` if a context could not be created. In Objective-C, you’re responsible for releasing this object using [`CGContextRelease`](cgcontextrelease.md).

#### Discussion

When you call this function, Core Graphics creates a PDF drawing environment—that is, a graphics context—to your specifications. When you draw into the resulting context, Core Graphics renders your drawing as a series of PDF drawing commands stored in the specified location.

## Parameters

- `url`: A Core Foundation URL that specifies where you want to place the resulting PDF file.
- `mediaBox`: A rectangle that specifies the bounds of the PDF. The origin of the rectangle should typically be  . The   function uses this rectangle as the default page media bounding box. If you pass  ,   uses a default page size of 8.5 by 11 inches (612 by 792 points).
- `auxiliaryInfo`: A dictionary that specifies any additional information to be used by the PDF context when generating the PDF file, or  . The dictionary is retained by the new context, so on return you may safely release it.

## See Also

- [init?(consumer: CGDataConsumer, mediaBox: UnsafePointer<CGRect>?, CFDictionary?)](cgcontext/init(consumer:mediabox:_:).md)
  Creates a PDF graphics context.
- [Auxiliary Dictionary Keys](auxiliary-dictionary-keys.md)
  Keys for the auxiliary info dictionary you specify when creating a PDF context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/init(_:mediabox:_:))*