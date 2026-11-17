# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The custom object you provide to handle controller-related events.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
weak var delegate: (any CPInstrumentClusterControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<CPInstrumentClusterControllerDelegate> delegate;
```

## Discussion

Assign a custom object to this property to receive information about events related to your instrument cluster UI. Make sure your custom object adopts the [`CPInstrumentClusterControllerDelegate`](../cpinstrumentclustercontrollerdelegate.md) protocol and implements the required methods. The controller notifies your delegate when the window changes, when vehicle settings change, and when the vehicle directs you to change the zoom level of your map content.

## See Also

### Managing the instrument cluster content
- [protocol CPInstrumentClusterControllerDelegate](../cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller/delegate)*