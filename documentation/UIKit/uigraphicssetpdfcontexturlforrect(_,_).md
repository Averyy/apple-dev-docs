# UIGraphicsSetPDFContextURLForRect(_:_:)

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Links a rectangular area on the current page to the specified URL.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsSetPDFContextURLForRect(_ url: URL, _ rect: CGRect)
```

```c
extern void UIGraphicsSetPDFContextURLForRect(NSURL *url, CGRect rect);
```

## Discussion

You use this function to create external links within a PDF document. If the URL you specify is a type handled by a different application, tapping the rectangle opens that application.

If the current graphics context is not a PDF context, this function does nothing.

## Parameters

- `url`: The URL to open.
- `rect`: A rectangle on the current page of the PDF context.

## See Also

### PDF creation
- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](./uigraphicsbeginpdfcontexttodata%28_,_,_%29.md)
  Creates a PDF graphics context that targets the specified mutable data object.
- [func UIGraphicsBeginPDFContextToFile(String, CGRect, [AnyHashable : Any]?) -> Bool](./uigraphicsbeginpdfcontexttofile%28_,_,_%29.md)
  Creates a PDF graphics context that targets a file at the specified path.
- [func UIGraphicsEndPDFContext()](./uigraphicsendpdfcontext%28%29.md)
  Closes a PDF graphics context and pops it from the current context stack.
- [func UIGraphicsBeginPDFPage()](./uigraphicsbeginpdfpage%28%29.md)
  Marks the beginning of a new page in a PDF context and configures it using default values.
- [func UIGraphicsBeginPDFPageWithInfo(CGRect, [AnyHashable : Any]?)](./uigraphicsbeginpdfpagewithinfo%28_,_%29.md)
  Marks the beginning of a new page in a PDF context and configures it using the specified custom values.
- [func UIGraphicsGetPDFContextBounds() -> CGRect](./uigraphicsgetpdfcontextbounds%28%29.md)
  Returns the current page bounds.
- [func UIGraphicsAddPDFContextDestinationAtPoint(String, CGPoint)](./uigraphicsaddpdfcontextdestinationatpoint%28_,_%29.md)
  Creates a jump destination in the current page.
- [func UIGraphicsSetPDFContextDestinationForRect(String, CGRect)](./uigraphicssetpdfcontextdestinationforrect%28_,_%29.md)
  Links a rectangular area on the current page to the specified jump destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicssetpdfcontexturlforrect(_:_:))*