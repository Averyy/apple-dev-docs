# propertyList

**Framework**: UIKit  
**Kind**: property

An object that contains data to associate with the key command.

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

#### Discussion

Use [`propertyList`](uikeycommand/propertylist.md) to associate a small amount of data to the command.

**Swift**:

In Swift, the property list should contain only standard library types such as [`Array`](https://developer.apple.com/documentation/Swift/Array), [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary), [`String`](https://developer.apple.com/documentation/Swift/String), [`Int`](https://developer.apple.com/documentation/Swift/Int), and [`Double`](https://developer.apple.com/documentation/Swift/Double), and Foundation types such as [`Date`](https://developer.apple.com/documentation/Foundation/Date) and [`Data`](https://developer.apple.com/documentation/Foundation/Data).

**Objective-C**:

In Objective-C, the property list should contain only [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), and [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) objects.

## See Also

- [let UICommandTagShare: String](uicommandtagshare.md)
  A value that identifies a command as a Share menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/propertylist)*