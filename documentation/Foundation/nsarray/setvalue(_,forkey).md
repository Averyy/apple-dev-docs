# setValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Invokes [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) on each of the array’s items using the specified `value` and `key`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setValue(_ value: Any?, forKey key: String)
```

```objc
- (void) setValue:(id) value forKey:(NSString *) key;
```

## Parameters

- `value`: The object value.
- `key`: The key to store the value.

## See Also

### Key-Value Coding
- [func value(forKey: String) -> Any](./value%28forkey%29.md)
  Returns an array containing the results of invoking [`value(forKey:)`](./value%28forkey%29.md) using `key` on each of the array’s objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/setvalue(_:forkey:))*