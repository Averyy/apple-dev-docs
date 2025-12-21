# callAsFunction(ageGates:_:_:)

**Framework**: Declared Age Range  
**Kind**: method

Returns a response indicating whether the person has set their age range.

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

This method handles the platform specific UI context retrieval and presents the age range request interface for the specific platform and view hierarchy.

The system may return geo-specific age ranges that override your provided age gates based on the person’s location and applicable regulations. When geo-specific ranges are required, the returned age range reflects region specific requirements rather than the bounds of your age gates.

Use doc://com.apple.documentation/documentation/SwiftUICore/EnvironmentValues/requestAgeRange with SwiftUI environment values to request age ranges in response to user interactions:

```swift
struct ContentView: View {
    @Environment(\.requestAgeRange) private var requestAgeRange
    @State private var ageRange: AgeRange?

    var body: some View {
        Button("Declare Age Range") {
            Task {
                do {
                    let response = try await requestAgeRange(ageGates: 13, 16, 18)
                    if case let .sharing(range) = response {
                        ageRange = range
                    }
                } catch {
                    // Handle error
                }
            }
        }
    }
}
```

> **Note**: An error if the request fails.

## Parameters

- `threshold1`: The primary age gate threshold for your app.
- `threshold2`: An optional second age threshold for additional content tiers.
- `threshold3`: An optional third age threshold for further content differentiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction/callasfunction(agegates:_:_:))*