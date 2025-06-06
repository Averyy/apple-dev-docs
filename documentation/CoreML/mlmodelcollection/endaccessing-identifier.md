# endAccessing(identifier:)

**Framework**: Core ML  
**Kind**: method

Terminates access to a model collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class func endAccessing(identifier: String) async throws -> Bool
```

#### Discussion

Use this method when your app no longer needs access to a model collection.

## Parameters

- `identifier`: The name of the model collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelcollection/endaccessing(identifier:))*