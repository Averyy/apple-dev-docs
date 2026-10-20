# activeStateIdentifier

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The identifier of the template’s current voice control state.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var activeStateIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * activeStateIdentifier;
```

## See Also

### Activating a State
- [func activateVoiceControlState(withIdentifier: String)](./activatevoicecontrolstate%28withidentifier%29.md)
  Changes the template’s state to the one matching the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate/activestateidentifier)*