# UIGraphicsGetPDFContextBounds()

**Framework**: UIKit  
**Kind**: func

Returns the current page bounds.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsGetPDFContextBounds() -> CGRect
```

#### Return Value

The current page bounds associated with the PDF context or [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero) if the current context is not a PDF context.

#### Discussion

If a page has not yet been started, this function returns the default media box you specified when you created the PDF context; otherwise, it returns the page bounds for the current page.

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
- [func UIGraphicsAddPDFContextDestinationAtPoint(String, CGPoint)](uigraphicsaddpdfcontextdestinationatpoint(_:_:).md)
  Creates a jump destination in the current page.
- [func UIGraphicsSetPDFContextDestinationForRect(String, CGRect)](uigraphicssetpdfcontextdestinationforrect(_:_:).md)
  Links a rectangular area on the current page to the specified jump destination.
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](uigraphicssetpdfcontexturlforrect(_:_:).md)
  Links a rectangular area on the current page to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsgetpdfcontextbounds())*