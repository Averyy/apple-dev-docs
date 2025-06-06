# accessoryUniqueIdentifiers

**Framework**: HomeKit  
**Kind**: property

The values corresponding to accessories that are set up.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Declaration

```swift
var accessoryUniqueIdentifiers: [UUID] { get }
```

#### Discussion

Usually only one accessory is set up at a time, but adding an accessory bridge can result in multiple accessories being set up at once. See [`uniqueIdentifier`](hmhome/uniqueidentifier.md) for more information.

## See Also

- [var homeUniqueIdentifier: UUID](hmaccessorysetupresult/homeuniqueidentifier.md)
  The home that accessories were added to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetupresult/accessoryuniqueidentifiers)*