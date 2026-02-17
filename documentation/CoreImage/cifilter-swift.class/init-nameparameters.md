# init(name:parameters:)

**Framework**: Core Image  
**Kind**: init

Creates a new filter of type ‘name’. The filter’s input parameters are set from the dictionary of key-value pairs. On OSX, any of the filter input parameters not specified in the dictionary will be undefined. On iOS, any of the filter input parameters not specified in the dictionary will be set to default values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(name: String, parameters params: [String : Any]?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(name:parameters:))*