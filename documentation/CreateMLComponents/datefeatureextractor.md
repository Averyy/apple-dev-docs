# DateFeatureExtractor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A time and date feature extractor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DateFeatureExtractor<Scalar> where Scalar : BinaryFloatingPoint
```

## Overview

This transformer takes a [`Date`](../Foundation/date.md) and extracts floating-point feature values according to the features parameter. Every feature value is roughly between -0.5 and 0.5. All date calculations are based on a [`Calendar`](../Foundation/calendar.md), which defaults to [`current`](../Foundation/calendar/current.md).

## Topics

### Creating a data feature extractor
- [init(features: DateFeatures, calendar: Calendar)](./datefeatureextractor/init%28features,calendar%29.md)
  Creates a date feature extractor.
### Applying a data feature extractor
- [func applied(to: Date, eventHandler: EventHandler?) -> [Scalar]](./datefeatureextractor/applied%28to,eventhandler%29.md)
  Extracts features of a particular date.
### Inspecting a data feature extractor
- [let calendar: Calendar](./datefeatureextractor/calendar.md)
  The calendar.
- [let features: DateFeatures](./datefeatureextractor/features.md)
  The date and time features.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Transformer](./transformer.md)

## See Also

### Time-based components
- [Creating a time-series classifier](./creating-a-time-series-classifier.md)
  Train a machine learning model to predict the class label of time-series signals.
- [Creating a time-series forecaster](./creating-a-time-series-forecaster.md)
  Forecast future data points by training a machine learning model using historical data.
- [struct DateFeatures](./datefeatures.md)
  A set of date and time features.
- [struct LinearTimeSeriesForecaster](./lineartimeseriesforecaster.md)
  A time-series forecasting estimator.
- [struct LinearTimeSeriesForecasterConfiguration](./lineartimeseriesforecasterconfiguration.md)
  The configuration for a linear time-series forecaster.
- [struct TimeSeriesForecasterBatches](./timeseriesforecasterbatches.md)
  A sequence of forecaster batches on a time series shaped array.
- [struct TimeSeriesForecasterAnnotatedWindows](./timeseriesforecasterannotatedwindows.md)
  A sequence of forecasting windows on a time series shaped array.
- [struct TemporalFeature](./temporalfeature.md)
  A temporal feature contains a segment identifier and a feature value.
- [protocol TemporalSequence](./temporalsequence.md)
  Async sequence for temporal features.
- [struct TemporalSegmentIdentifier](./temporalsegmentidentifier.md)
  Uniquely identifiers a segment of a temporal sequence.
- [struct SlidingWindows](./slidingwindows.md)
  A sequence of windows on a time series shaped array.
- [struct SlidingWindowTransformer](./slidingwindowtransformer.md)
  A temporal transformer that groups input elements.
- [struct Downsampler](./downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](./videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](./temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/datefeatureextractor)*