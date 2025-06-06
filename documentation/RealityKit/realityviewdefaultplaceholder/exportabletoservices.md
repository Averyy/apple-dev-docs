# exportableToServices(_:)

**Framework**: RealityKit  
**Kind**: method

Exports items for consumption by shortcuts, quick actions, and services.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
func exportableToServices<T>(_ payload: @autoclosure @escaping () -> [T]) -> some View where T : Transferable
```

#### Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

```None
var title: String
var body: some View {
    Color.pink
        .frame(width: 400, height: 400)
        .exportableToServices([title])
}
```

## Parameters

- `payload`: A closure that will be called on request of the items   by the shortcut or service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/exportabletoservices(_:))*