# workoutPreview(_:isPresented:)

**Framework**: SwiftUI  
**Kind**: method

Presents a preview of the workout contents as a modal sheet

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func workoutPreview(_ workout: WorkoutPlan, isPresented: Binding<Bool>) -> some View
```

#### Discussion

```swift
struct WorkoutPreviewer: View {
    let workout: WorkoutPlan
    @State var presented: Bool = false
    var body: some View {
        Button {
            isPresented = true
        } label: {
            WorkoutContainerView(workout)
        }
        .workoutPreview(workout, isPresented: $presented)
    }
}
```

## Parameters

- `workout`: The   the preview displays
- `isPresented`: A binding to a Boolean value that determines whether to present the preview

## See Also

- [func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType, predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:).md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func healthDataAccessRequest(store: HKHealthStore, readTypes: Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:readtypes:trigger:completion:).md)
  Requests permission to read the specified HealthKit data types.
- [func healthDataAccessRequest(store: HKHealthStore, shareTypes: Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:).md)
  Requests permission to save and read the specified HealthKit data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/workoutpreview(_:ispresented:))*