# coerceValue(_:forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Uses type info from the class description and `NSScriptCoercionHandler` to attempt to convert `value` for `key` to the proper type, if necessary.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func coerceValue(_ value: Any?, forKey key: String) -> Any?
```

#### Discussion

The method `coerceValueFor<Key>:` is used if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/coercevalue(_:forkey:))*