# eventDidFail(_:withError:)

**Framework**: Scripting Bridge  
**Kind**: method  
**Required**: Yes

Sent by an `SBApplication` object when a target application returns an error Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: any Error) -> Any?
```

#### Return Value

If you return a result, it will become the result of the [`sendEvent(_:)`](https://developer.apple.com/documentation/AppKit/NSApplication/sendEvent(_:)) that failed. Can be `nil`.

## Parameters

- `event`: A pointer to the Apple event sent to the target application causing   the error.
- `error`: An object containing information about the error Apple event.   Specific information may be included in the   dictionary of the   error object. The following table shows the possible   keys for this dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate/eventdidfail(_:witherror:))*