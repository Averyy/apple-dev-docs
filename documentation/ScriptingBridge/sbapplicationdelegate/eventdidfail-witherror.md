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

If you return a result, it will become the result of the [`sendEvent(_:)`](https://developer.apple.com/documentation/appkit/nsapplication/sendevent(_:)) that failed. Can be `nil`.

## Parameters

- `event`: A pointer to the Apple event sent to the target application causing the error.
- `error`: An object containing information about the error Apple event. Specific information may be included in the `useInfo` dictionary of the error object. The following table shows the possible keys for this dictionary. | Key | Description |
| --- | --- |
| ErrorBriefMessage | A short human-readable description of the error, as an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) |
| ErrorExpectedType | The type of data the target application expected, as an [`NSAppleEventDescriptor`](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor) object. |
| ErrorOffendingObject | The object that caused the error. |
| ErrorString | A full human-readable description of the error, as an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) object. |
| ErrorNumber | The Apple event error number, as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object. |


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate/eventdidfail(_:witherror:))*