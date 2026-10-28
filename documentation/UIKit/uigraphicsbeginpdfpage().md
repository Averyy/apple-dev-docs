# UIGraphicsBeginPDFPage()

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Marks the beginning of a new page in a PDF context and configures it using default values.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsBeginPDFPage()
```

```c
extern void UIGraphicsBeginPDFPage();
```

## Discussion

This function ends any previous page before beginning a new one. It sets the media box of the new page to the rectangle you specified when you created the PDF context.

If the current graphics context is not a PDF context, this function does nothing.

You must call this function or the [`UIGraphicsBeginPDFPageWithInfo(_:_:)`](./uigraphicsbeginpdfpagewithinfo%28_,_%29.md) function before you issue any drawing commands.

## See Also

### PDF creation
- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](./uigraphicsbeginpdfcontexttodata%28_,_,_%29.md)
  Creates a PDF graphics context that targets the specified mutable data object.
- [func UIGraphicsBeginPDFContextToFile(String, CGRect, [AnyHashable : Any]?) -> Bool](./uigraphicsbeginpdfcontexttofile%28_,_,_%29.md)
  Creates a PDF graphics context that targets a file at the specified path.
- [func UIGraphicsEndPDFContext()](./uigraphicsendpdfcontext%28%29.md)
  Closes a PDF graphics context and pops it from the current context stack.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginpdfpage())*