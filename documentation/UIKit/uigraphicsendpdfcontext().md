# UIGraphicsEndPDFContext()

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Closes a PDF graphics context and pops it from the current context stack.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsEndPDFContext()
```

```c
extern void UIGraphicsEndPDFContext();
```

#### Discussion

You must call this function after you finish drawing to a PDF graphics context. This function closes the current open page and removes the PDF context from the graphics context stack. It also releases the [`CGContext`](../CoreGraphics/cgcontext.md) associated with the PDF context.  If the current graphics context is not a PDF context, this function does nothing.

## See Also

### PDF creation
- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](./uigraphicsbeginpdfcontexttodata%28_,_,_%29.md)
  Creates a PDF graphics context that targets the specified mutable data object.
- [func UIGraphicsBeginPDFContextToFile(String, CGRect, [AnyHashable : Any]?) -> Bool](./uigraphicsbeginpdfcontexttofile%28_,_,_%29.md)
  Creates a PDF graphics context that targets a file at the specified path.
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
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](./uigraphicssetpdfcontexturlforrect%28_,_%29.md)
  Links a rectangular area on the current page to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsendpdfcontext())*