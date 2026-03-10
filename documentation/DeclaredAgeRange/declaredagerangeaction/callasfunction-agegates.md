# callAsFunction(ageGates:_:_:)

**Framework**: Declared Age Range  
**Kind**: method

Returns a response indicating whether the person shared their age range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func callAsFunction(ageGates threshold1: Int, _ threshold2: Int? = nil, _ threshold3: Int? = nil) async throws -> AgeRangeService.Response
```

#### Return Value

A response indicating whether the person declared their age range. If the person shared their age range, the system also returns the age range.

#### Discussion

Regional requirements may override your age gates based on the person’s location.

Use [`requestAgeRange`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/requestAgeRange) with SwiftUI environment values to request age ranges in response to user interactions:

```swift
struct ContentView: View {
    @Environment(\.requestAgeRange) var requestAgeRange

    var body: some View {
        Button("Check Age Range") {
            Task {
                do {
                    let response = try await requestAgeRange(ageGates: 13, 16, 18)
                    switch response {
                    case let .sharing(ageRange):
                        // Person shared their age range.
                        break
.                    case .declinedSharing:
                        // In regulated regions, the system automatically provides the person's age range — the person can't decline sharing.
                        break
                    }
                } catch {
                    // Handle error.
                }
            }
        }
    }
}
```

> **Note**: An error if the request fails.

## Parameters

- `threshold1`: The primary age threshold for your app.
- `threshold2`: An optional second age threshold that creates an additional age range.
- `threshold3`: An optional third age threshold that creates a final age range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction/callasfunction(agegates:_:_:))*