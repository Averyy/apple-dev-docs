# fulfill()

**Framework**: CallKit  
**Kind**: method

Reports the successful execution of the action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func fulfill()
```

## Mentions

- [Making and receiving VoIP calls](making-and-receiving-voip-calls.md)

#### Discussion

Calling this method sets the [`isComplete`](cxaction/iscomplete.md) property value to [`true`](https://developer.apple.com/documentation/Swift/true). Calling this method more than once or calling it after calling the [`fail()`](cxaction/fail().md) method has no effect.

It’s safe to call `fulfill()` asynchronously. For example, call it in [`CXProviderDelegate`](cxproviderdelegate.md) callback method implementations as shown in the following code snippet from the [`Making and receiving VoIP calls`](making-and-receiving-voip-calls.md) sample code project:

```swift
func provider(_ provider: CXProvider, perform action: CXStartCallAction) {
    //
    // ...
    //
    // Trigger the call to be started via the underlying network service.
    call.startSpeakerboxCall { success in
        if success {
            // Signal to the system that the action was successfully performed.
            action.fulfill()

            // ...
        } else {
            // Signal to the system that the action was unable to be performed.
            action.fail()
        }
    }
}
```

## See Also

- [func fail()](cxaction/fail.md)
  Reports the failed execution of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction/fulfill())*