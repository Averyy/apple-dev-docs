# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a user activity object using the first activity type declared in the app’s information property list file.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.12
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use initWithActivityType: with a specific activity type string

## Declaration

```swift
convenience init()
```

```objc
- (instancetype) init;
```

#### Return Value

An [`NSUserActivity`](../nsuseractivity.md) object.

#### Discussion

This method retrieves the first string of the [NSUserActivityTypes](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW28) key declared in the app’s `Info.plist` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/init())*