# DateFeatures

**Framework**: Create ML Components  
**Kind**: struct

A set of date and time features.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DateFeatures
```

#### Overview

The choice of features for a particular task depends on the relevance of different date and time components. For example a dataset of weather data may require hour and day-of-year features, while a dataset of workout metrics may require second, hour, and weekday features.

## Topics

### Initializers
- [init(rawValue: Int)](datefeatures/init(rawvalue:).md)
  Creates a feature from a raw value.
### Instance Properties
- [var rawValue: Int](datefeatures/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [DateFeatures.ArrayLiteralElement](datefeatures/arrayliteralelement.md)
  The type of the elements of an array literal.
- [DateFeatures.Element](datefeatures/element.md)
  The element type of the option set.
- [DateFeatures.RawValue](datefeatures/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let day: DateFeatures](datefeatures/day.md)
  A feature representing the day within the month.
- [static let dayOfYear: DateFeatures](datefeatures/dayofyear.md)
  A feature representing the day within the year.
- [static let hour: DateFeatures](datefeatures/hour.md)
  A feature representing the hour within the day.
- [static let minute: DateFeatures](datefeatures/minute.md)
  A feature representing the minute within the hour.
- [static let month: DateFeatures](datefeatures/month.md)
  A feature representing the month within the year.
- [static let second: DateFeatures](datefeatures/second.md)
  A feature representing the second within the minute.
- [static let weekOfMonth: DateFeatures](datefeatures/weekofmonth.md)
  A feature representing the week within the month.
- [static let weekOfYear: DateFeatures](datefeatures/weekofyear.md)
  A feature representing the week within the year.
- [static let weekday: DateFeatures](datefeatures/weekday.md)
  A feature representing the weekday.
### Default Implementations
- [Equatable Implementations](datefeatures/equatable-implementations.md)
- [OptionSet Implementations](datefeatures/optionset-implementations.md)
- [RawRepresentable Implementations](datefeatures/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](datefeatures/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Creating a time-series classifier](creating-a-time-series-classifier.md)
  Train a machine learning model to predict the class label of time-series signals.
- [Creating a time-series forecaster](creating-a-time-series-forecaster.md)
  Forecast future data points by training a machine learning model using historical data.
- [struct DateFeatureExtractor](datefeatureextractor.md)
  A time and date feature extractor.
- [struct LinearTimeSeriesForecaster](lineartimeseriesforecaster.md)
  A time-series forecasting estimator.
- [struct LinearTimeSeriesForecasterConfiguration](lineartimeseriesforecasterconfiguration.md)
  The configuration for a linear time-series forecaster.
- [struct TimeSeriesForecasterBatches](timeseriesforecasterbatches.md)
  A sequence of forecaster batches on a time series shaped array.
- [struct TimeSeriesForecasterAnnotatedWindows](timeseriesforecasterannotatedwindows.md)
  A sequence of forecasting windows on a time series shaped array.
- [struct TemporalFeature](temporalfeature.md)
  A temporal feature contains a segment identifier and a feature value.
- [protocol TemporalSequence](temporalsequence.md)
  Async sequence for temporal features.
- [struct TemporalSegmentIdentifier](temporalsegmentidentifier.md)
  Uniquely identifiers a segment of a temporal sequence.
- [struct SlidingWindows](slidingwindows.md)
  A sequence of windows on a time series shaped array.
- [struct SlidingWindowTransformer](slidingwindowtransformer.md)
  A temporal transformer that groups input elements.
- [struct Downsampler](downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/datefeatures)*