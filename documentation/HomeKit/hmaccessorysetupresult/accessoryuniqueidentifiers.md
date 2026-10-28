# accessoryUniqueIdentifiers

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The values corresponding to accessories that are set up.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 27.0+

## Declaration

```swift
var accessoryUniqueIdentifiers: [UUID] { get }
```

```objc
@property (copy, readonly) NSArray<NSUUID *> * accessoryUniqueIdentifiers;
```

## Discussion

Usually only one accessory is set up at a time, but adding an accessory bridge can result in multiple accessories being set up at once. See [`uniqueIdentifier`](../hmhome/uniqueidentifier.md) for more information.

## See Also

### Getting results
- [var homeUniqueIdentifier: UUID](./homeuniqueidentifier.md)
  The home that accessories were added to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetupresult/accessoryuniqueidentifiers)*