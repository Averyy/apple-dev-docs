# reinterpret_pointer_cast

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
template <typename T_, typename U, typename Policy> bounded_ptr<T_, Policy> reinterpret_pointer_cast(const bounded_ptr<U, Policy> & ) noexcept;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/reinterpret_pointer_cast-1viq2)*