# valueLength

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

The number of bytes in the value field.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var valueLength: Int
```

```c
size_t valueLength;
```

## Discussion

Set this field to `0` if you set the `value` field to `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationitem/valuelength)*