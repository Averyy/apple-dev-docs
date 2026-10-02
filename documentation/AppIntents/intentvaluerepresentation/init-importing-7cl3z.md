# init(importing:)

**Framework**: App Intents  
**Kind**: init

Creates a value representation that imports a system intent value into an entity.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
init(importing: @escaping @Sendable (IntentValue) async throws -> Item)
```

#### Discussion

Use this initializer when your entity can be created from a system type, but has no meaningful representation to export back out. The entity’s metadata declares the system type as importable only, and the entity is never offered for export as that type.

#### Example

```swift
struct LocationEntity: AppEntity, Transferable {
    static var transferRepresentation: some TransferRepresentation {
        IntentValueRepresentation(
            importing: { place in
                guard let coordinate = place.coordinate else {
                    throw ImportError.missingCoordinate
                }
                return LocationEntity(
                    name: place.commonName ?? "Unknown Location",
                    latitude: coordinate.latitude,
                    longitude: coordinate.longitude
                )
            }
        )
    }
}
```

## Parameters

- `importing`: A closure that converts a system intent value to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluerepresentation/init(importing:)-7cl3z)*