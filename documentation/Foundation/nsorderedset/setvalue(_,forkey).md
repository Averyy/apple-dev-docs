# setValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Invokes `setValue:forKey:` on each of the receiver’s members using the specified value and key

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
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

### Key-Value Coding Support
- [func value(forKey: String) -> Any](./value%28forkey%29.md)
  Returns an ordered set containing the results of invoking `valueForKey:` using key on each of the ordered set’s objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/setvalue(_:forkey:))*