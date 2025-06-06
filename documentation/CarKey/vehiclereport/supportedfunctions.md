# supportedFunctions

**Framework**: CarKey  
**Kind**: property

An array of function identifiers that indicates the features the vehicle supports, populated only after the first BLE connection with the vehicle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
var supportedFunctions: [FunctionIdentifier] { get }
```

#### Discussion

When building your app’s UI, use the information in this property to determine what features you can access. The array contains all supported features. To determine if a feature is currently supported, call the [`status(for:)`](vehiclereport/status(for:).md) method.

## See Also

- [func status(for: FunctionIdentifier) throws -> FunctionStatus?](vehiclereport/status(for:).md)
  Returns the current status of the specified vehicle function.
- [struct FunctionStatus](functionstatus.md)
  A value that the vehicle can return to indicate the status of a particular vehicle feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/vehiclereport/supportedfunctions)*