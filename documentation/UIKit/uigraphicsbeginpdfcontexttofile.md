# UIGraphicsBeginPDFContextToFile(_:_:_:)

**Framework**: UIKit  
**Kind**: func

Creates a PDF graphics context that targets a file at the specified path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsBeginPDFContextToFile(_ path: String, _ bounds: CGRect, _ documentInfo: [AnyHashable : Any]?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the PDF context was created successfully or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

After creating the graphics context, this function makes it the current drawing context. Any subsequent drawing commands are therefore captured and turned into PDF data. When you are done drawing, you must call the [`UIGraphicsEndPDFContext()`](uigraphicsendpdfcontext().md) function to close the PDF graphics context.

You can use all of the same drawing routines that you would normally use to draw the contents of your application. However, before you issue any drawing commands to a PDF context, you must start a new page by calling the [`UIGraphicsBeginPDFPage()`](uigraphicsbeginpdfpage().md) or [`UIGraphicsBeginPDFPageWithInfo(_:_:)`](uigraphicsbeginpdfpagewithinfo(_:_:).md) function. You can also use these functions to define additional pages later.

After creating it, you can get the PDF context using the [`UIGraphicsGetCurrentContext()`](uigraphicsgetcurrentcontext().md) function.

## Parameters

- `path`: A POSIX-style path string identifying the location of the resulting PDF file. The specified path may be relative or a full path name. If a file does not exist at the specified path, one is created; otherwise, the contents of any existing file are deleted. The directories in the path must exist.
- `bounds`: A rectangle that specifies the default size and location of PDF pages. (This value is used as the default media box for each new page.) The origin of the rectangle should typically be (0, 0). Specifying an empty rectangle ( ) sets the default page size to 8.5 by 11 inches (612 by 792 points).
- `documentInfo`: Specify   if you do not want to associate any additional information with the PDF document.

## See Also

- [func UIGraphicsBeginPDFContextToData(NSMutableData, CGRect, [AnyHashable : Any]?)](uigraphicsbeginpdfcontexttodata(_:_:_:).md)
  Creates a PDF graphics context that targets the specified mutable data object.
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
- [func UIGraphicsSetPDFContextDestinationForRect(String, CGRect)](uigraphicssetpdfcontextdestinationforrect(_:_:).md)
  Links a rectangular area on the current page to the specified jump destination.
- [func UIGraphicsSetPDFContextURLForRect(URL, CGRect)](uigraphicssetpdfcontexturlforrect(_:_:).md)
  Links a rectangular area on the current page to the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginpdfcontexttofile(_:_:_:))*