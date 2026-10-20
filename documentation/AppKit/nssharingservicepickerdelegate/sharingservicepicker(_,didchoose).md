# sharingServicePicker(_:didChoose:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the person selected a sharing service for the current item.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func sharingServicePicker(_ sharingServicePicker: NSSharingServicePicker, didChoose service: NSSharingService?)
```

```objc
- (void) sharingServicePicker:(NSSharingServicePicker *) sharingServicePicker didChooseSharingService:(NSSharingService *) service;
```

#### Discussion

After someone chooses a service, the sharing service picker calls this method to let you know which service they picked. The sharing service receives the item sometime after this method returns.

## Parameters

- `sharingServicePicker`: The sharing service picker.
- `service`: The selected sharing service. Invoked to give the delegate to the sharing service that is about to be executed.

## See Also

### Customizing Behavior
- [func sharingServicePicker(NSSharingServicePicker, delegateFor: NSSharingService) -> (any NSSharingServiceDelegate)?](./sharingservicepicker%28_,delegatefor%29.md)
  Asks your delegate to provide an object that the selected sharing service can use as its delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservicepickerdelegate/sharingservicepicker(_:didchoose:))*