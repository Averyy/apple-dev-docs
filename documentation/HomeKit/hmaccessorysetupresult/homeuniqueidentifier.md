# homeUniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The home that accessories were added to.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 27.0+

## Declaration

```swift
var homeUniqueIdentifier: UUID { get }
```

```objc
@property (copy, readonly) NSUUID * homeUniqueIdentifier;
```

#### Discussion

See [`uniqueIdentifier`](../hmhome/uniqueidentifier.md) for more information.

## See Also

### Getting results
- [var accessoryUniqueIdentifiers: [UUID]](./accessoryuniqueidentifiers.md)
  The values corresponding to accessories that are set up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetupresult/homeuniqueidentifier)*