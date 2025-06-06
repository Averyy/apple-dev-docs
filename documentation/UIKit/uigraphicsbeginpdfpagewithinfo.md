# UIGraphicsBeginPDFPageWithInfo(_:_:)

**Framework**: UIKit  
**Kind**: func

Marks the beginning of a new page in a PDF context and configures it using the specified custom values.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsBeginPDFPageWithInfo(_ bounds: CGRect, _ pageInfo: [AnyHashable : Any]?)
```

#### Discussion

This function ends any previous page before beginning a new one. It sets the media box of the new page to the value in the [`kCGPDFContextMediaBox`](https://developer.apple.com/documentation/CoreGraphics/kCGPDFContextMediaBox) key of the `pageInfo` dictionary, or to the value in the `bounds` parameter if the dictionary does not contain the key.

If the current graphics context is not a PDF context, this function does nothing.

You must call this function or the [`UIGraphicsBeginPDFPageWithInfo(_:_:)`](uigraphicsbeginpdfpagewithinfo(_:_:).md) function before you issue any drawing commands.

## Parameters

- `bounds`: A rectangle that specifies the size and location of the new PDF page. This rectangle corresponds to the media box rectangle for the page.
- `pageInfo`: Specify   if you do not want to associate any additional information with the page.

## See Also

- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](uigraphicsbeginpdfcontexttodata(_:_:_:).md)
  Creates a PDF graphics context that targets the specified mutable data object.
- [func UIGraphicsBeginPDFContextToFile(String, CGRect, [AnyHashable : Any]?) -> Bool](uigraphicsbeginpdfcontexttofile(_:_:_:).md)
  Creates a PDF graphics context that targets a file at the specified path.
- [func UIGraphicsEndPDFContext()](uigraphicsendpdfcontext().md)
  Closes a PDF graphics context and pops it from the current context stack.
- [func UIGraphicsBeginPDFPage()](uigraphicsbeginpdfpage().md)
  Marks the beginning of a new page in a PDF context and configures it using default values.
- [func UIGraphicsGetPDFContextBounds() -> CGRect](uigraphicsgetpdfcontextbounds().md)
  Returns the current page bounds.
- [func UIGraphicsAddPDFContextDestinationAtPoint(String, CGPoint)](uigraphicsaddpdfcontextdestinationatpoint(_:_:).md)
  Creates a jump destination in the current page.
- [func UIGraphicsSetPDFContextDestinationForRect(String, CGRect)](uigraphicssetpdfcontextdestinationforrect(_:_:).md)
  Links a rectangular area on the current page to the specified jump destination.
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](uigraphicssetpdfcontexturlforrect(_:_:).md)
  Links a rectangular area on the current page to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginpdfpagewithinfo(_:_:))*