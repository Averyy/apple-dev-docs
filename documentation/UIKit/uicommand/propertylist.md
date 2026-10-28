# propertyList

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that contains data to associate with the command.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var propertyList: Any? { get }
```

```objc
@property (nonatomic, readonly, nullable) id propertyList;
```

## Discussion

Use [`propertyList`](./propertylist.md) to associate a small amount of data to the command.

**Swift**:

In Swift, the property list should contain only standard library types such as [`Array`](../../Swift/array.md), [`Dictionary`](../../Swift/dictionary.md), [`String`](../../Swift/string.md), [`Int`](../../Swift/int.md), and [`Double`](../../Swift/double.md), and Foundation types such as [`Date`](../../Foundation/date.md) and [`Data`](../../Foundation/data.md).

**Objective-C**:

In Objective-C, the property list should contain only [`NSArray`](../../Foundation/nsarray.md), [`NSDictionary`](../../Foundation/nsdictionary.md), [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), [`NSDate`](../../Foundation/nsdate.md), and [`NSData`](../../Foundation/nsdata.md) objects.

## See Also

### Associating data
- [let UICommandTagShare: String](../uicommandtagshare.md)
  A value that identifies a command as a Share menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicommand/propertylist)*