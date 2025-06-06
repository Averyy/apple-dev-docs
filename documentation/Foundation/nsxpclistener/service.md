# service()

**Framework**: Foundation  
**Kind**: method

Returns the singleton listener used to listen for incoming connections in an XPC service.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func service() -> NSXPCListener
```

#### Discussion

Calling the `resume` method on the returned object starts the listener and never returns. This method is typically called at the end of your `main` function.

> **Note**:  This method requires that the XPC service has the appropriate configuration in its `Info.plist` file.

 This method requires that the XPC service has the appropriate configuration in its `Info.plist` file.

## See Also

- [class func anonymous() -> NSXPCListener](nsxpclistener/anonymous.md)
  Returns a new anonymous listener connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener/service())*