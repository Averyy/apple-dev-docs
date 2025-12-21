# PropertyListenerDelegate

**Framework**: Core Audio  
**Kind**: protocol

A delegate protocol for receiving notifications when properties registered with AudioHardwareObject.addPropertyListener change.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
protocol PropertyListenerDelegate
```

## Topics

### Instance Methods
- [func propertiesChanged(properties: [AudioObjectPropertyAddress])](propertylistenerdelegate/propertieschanged(properties:).md)
  Called when registered properties change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/propertylistenerdelegate)*