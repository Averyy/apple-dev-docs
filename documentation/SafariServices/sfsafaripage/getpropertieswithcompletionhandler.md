# getPropertiesWithCompletionHandler(_:)

**Framework**: Safari Services  
**Kind**: method

Retrieves the properties of the webpage.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func properties() async -> SFSafariPageProperties?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func properties() async -> SFSafariPageProperties?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If the extension cannot access the page—for example, the extension has web access permissions set to `None` in the Info.plist—the properties object passed to the completion handler is `nil`. See [`SFSafariPageProperties`](sfsafaripageproperties.md).

## Parameters

- `completionHandler`: A block to call when the properties object is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage/getpropertieswithcompletionhandler(_:))*