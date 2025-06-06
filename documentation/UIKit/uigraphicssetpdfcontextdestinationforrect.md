# UIGraphicsSetPDFContextDestinationForRect(_:_:)

**Framework**: UIKit  
**Kind**: func

Links a rectangular area on the current page to the specified jump destination.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsSetPDFContextDestinationForRect(_ name: String, _ rect: CGRect)
```

#### Discussion

You use this function to create live links within a PDF document. Tapping the specified rectangle in the PDF document causes the document to display the contents at the associated jump destination.

If the current graphics context is not a PDF context, this function does nothing.

## Parameters

- `name`: A named destination in the PDF document. This is the same name you used when creating the jump destination using the   function.
- `rect`: A rectangle on the current page of the PDF context.

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
- [func UIGraphicsAddPDFContextDestinationAtPoint(String, CGPoint)](uigraphicsaddpdfcontextdestinationatpoint(_:_:).md)
  Creates a jump destination in the current page.
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](uigraphicssetpdfcontexturlforrect(_:_:).md)
  Links a rectangular area on the current page to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicssetpdfcontextdestinationforrect(_:_:))*