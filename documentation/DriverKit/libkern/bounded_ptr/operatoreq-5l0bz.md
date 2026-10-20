# operator=

**Framework**: DriverKit  
**Kind**: method  
**Role**: Method Template

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
template <typename U, typename Policy, typename = detail::detail::enable_if_t<detail::is_convertible_v<U *, T *>>> bounded_ptr<T, TrappingPolicy> & operator=(const bounded_ptr<U, Policy> & other);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/libkern/bounded_ptr/operator=-5l0bz)*