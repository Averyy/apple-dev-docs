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
template <typename T, typename U, typename Policy> bounded_ptr<T, Policy> reinterpret_pointer_cast(const bounded_ptr<U, Policy> & p) noexcept;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/reinterpret_pointer_cast-7u0yk)*