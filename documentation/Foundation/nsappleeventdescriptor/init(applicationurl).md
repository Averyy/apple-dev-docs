# init(applicationURL:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates and returns an application address descriptor using the specified application URL.

**Availability**:
- macOS 10.11+

## Declaration

```swift
init(applicationURL: URL)
```

```objc
+ (NSAppleEventDescriptor *) descriptorWithApplicationURL:(NSURL *) applicationURL;
```

#### Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(applicationurl:))*