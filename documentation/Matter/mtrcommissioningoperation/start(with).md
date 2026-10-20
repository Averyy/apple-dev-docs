# start(with:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Start commissioning with the given controller (which identifies the fabric the commissionee should be commissioned into).  The delegate will be notified if there are any failures.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
func start(with controller: MTRDeviceController)
```

```objc
- (void) startWithController:(MTRDeviceController *) controller;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningoperation/start(with:))*