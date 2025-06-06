# UIGraphicsAddPDFContextDestinationAtPoint(_:_:)

**Framework**: UIKit  
**Kind**: func

Creates a jump destination in the current page.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsAddPDFContextDestinationAtPoint(_ name: String, _ point: CGPoint)
```

#### Discussion

This function marks the specified point in the current page as the destination of a jump. When the user taps a link that takes them to this jump destination, the PDF document scrolls until the specified point is visible.

If the current graphics context is not a PDF context, this function does nothing.

For information on how to create links to this destination, see the [`UIGraphicsSetPDFContextDestinationForRect(_:_:)`](uigraphicssetpdfcontextdestinationforrect(_:_:).md) function.

## Parameters

- `name`: The name of the destination point. The name you assign is local to the PDF document and is what you use when creating links to this destination.
- `point`: A point on the current page of the PDF context.

## See Also

- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](uigraphicsbeginpdfcontexttodata(_:_:_:).md)
  Creates a PDF graphics context that targets the specified mutable data object.
- [func UIGraphicsBeginPDFContextToFile(String, CGRect, [AnyHashable : Any]?) -> Bool](uigraphicsbeginpdfcontexttofile(_:_:_:).md)
  Creates a PDF graphics context that targets a file at the specified path.
- [func UIGraphicsEndPDFContext()](uigraphicsendpdfcontext().md)
  Closes a PDF graphics context and pops it from the current context stack.
- [func UIGraphicsBeginPDFPage()](uigraphicsbeginpdfpage().md)
  Marks the beginning of a new page in a PDF context and configures it using default values.
- [func UIGraphicsBeginPDFPageWithInfo(CGRect, [AnyHashable : Any]?)](uigraphicsbeginpdfpagewithinfo(_:_:).md)
  Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [func UIGraphicsGetPDFContextBounds() -> CGRect](uigraphicsgetpdfcontextbounds().md)
  Returns the current page bounds.
- [func UIGraphicsSetPDFContextDestinationForRect(String, CGRect)](uigraphicssetpdfcontextdestinationforrect(_:_:).md)
  Links a rectangular area on the current page to the specified jump destination.
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](uigraphicssetpdfcontexturlforrect(_:_:).md)
  Links a rectangular area on the current page to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsaddpdfcontextdestinationatpoint(_:_:))*