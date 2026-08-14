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

In Swift, the property list should contain only standard library types such as [`Array`](https://developer.apple.com/documentation/swift/array), [`Dictionary`](https://developer.apple.com/documentation/swift/dictionary), [`String`](https://developer.apple.com/documentation/swift/string), [`Int`](https://developer.apple.com/documentation/swift/int), and [`Double`](https://developer.apple.com/documentation/swift/double), and Foundation types such as [`Date`](https://developer.apple.com/documentation/foundation/date) and [`Data`](https://developer.apple.com/documentation/foundation/data).

**Objective-C**:

In Objective-C, the property list should contain only [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray), [`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary), [`NSString`](https://developer.apple.com/documentation/foundation/nsstring), [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber), [`NSDate`](https://developer.apple.com/documentation/foundation/nsdate), and [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) objects.

## See Also

- [let UICommandTagShare: String](uicommandtagshare.md)
  A value that identifies a command as a Share menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/propertylist)*