# SCNetworkReachabilityContext

**Framework**: System Configuration  
**Kind**: struct  
**Role**: Structure

Structure containing user-specified data and callbacks used with [`SCNetworkReachabilitySetCallback(_:_:_:)`](./scnetworkreachabilitysetcallback%28_,_,_%29.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct SCNetworkReachabilityContext
```

```c
typedef struct { ... } SCNetworkReachabilityContext;
```

## Topics

### Initializers
- [init()](./scnetworkreachabilitycontext/init%28%29.md)
  Creates a network reachability context.
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](./scnetworkreachabilitycontext/init%28version,info,retain,release,copydescription%29.md)
  Creates a network reachability context with the specified values.
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?](./scnetworkreachabilitycontext/copydescription.md)
  The callback used to provide a description of the `info` field.
- [var info: UnsafeMutableRawPointer?](./scnetworkreachabilitycontext/info.md)
  A C pointer to a user-specified block of data.
- [var release: ((UnsafeRawPointer) -> Void)?](./scnetworkreachabilitycontext/release.md)
  The callback used to remove a retain previously added for the info field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value can be `NULL`.
- [var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?](./scnetworkreachabilitycontext/retain.md)
  The callback used to add a retain for the info field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value can be `NULL`.
- [var version: CFIndex](./scnetworkreachabilitycontext/version.md)
  The version number of the structure type being passed in as a parameter to an `SCDynamicStore` creation function. This structure is version `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Data Types
- [class SCNetworkReachability](./scnetworkreachability.md)
  The handle to a network address or name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycontext)*