# sharingServicePicker(_:delegateFor:)

**Framework**: AppKit  
**Kind**: method

Asks your delegate to provide an object that the selected sharing service can use as its delegate.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func sharingServicePicker(_ sharingServicePicker: NSSharingServicePicker, delegateFor sharingService: NSSharingService) -> (any NSSharingServiceDelegate)?
```

#### Return Value

An object that adopts the [`NSSharingServiceDelegate`](nssharingservicedelegate.md) protocol.

#### Discussion

The sharing service assigns the returned object to its [`delegate`](nssharingservice/delegate.md) property.

## Parameters

- `sharingServicePicker`: The sharing service picker.
- `sharingService`: The selected sharing service.

## See Also

- [func sharingServicePicker(NSSharingServicePicker, didChoose: NSSharingService?)](nssharingservicepickerdelegate/sharingservicepicker(_:didchoose:).md)
  Tells the delegate that the person selected a sharing service for the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/sharingservicepicker(_:delegatefor:))*