# Tips

**Framework**: TipKit  
**Kind**: enum

TipKit namespace.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
enum Tips
```

#### Overview

A collection of objects for controlling the display of your tips.

## Topics

### Actions
- [struct Action](tips/action.md)
  A type that describes a control associated with a tip.
### Events
- [struct DonationTimeRange](tips/donationtimerange.md)
  A duration of time for filtering event donations.
- [struct EmptyDonation](tips/emptydonation.md)
  An empty event donation.
### Options
- [struct IgnoresDisplayFrequency](tips/ignoresdisplayfrequency.md)
  Controls whether a tip obeys the preconfigured display frequency interval.
- [struct MaxDisplayCount](tips/maxdisplaycount.md)
  Specifies the maximum number of times a tip displays before the system automatically invalidates it.
- [struct ConfigurationOption](tips/configurationoption.md)
  A type that marks an object as a tip configuration.
- [struct ParameterOption](tips/parameteroption.md)
  A type that represents the various customizations that you can make to a tip parameter.
### Builders
- [struct ActionBuilder](tips/actionbuilder.md)
  The result builder for generating a tip’s actions.
- [struct OptionsBuilder](tips/optionsbuilder.md)
  The result builder for generating a tip’s options.
- [struct RuleBuilder](tips/rulebuilder.md)
  The result builder for generating a tip’s rules.
### Status
- [Tips.Status](tips/status.md)
  A type that describes the current display eligibility status for a tip.
### Validation
- [Tips.InvalidationReason](tips/invalidationreason.md)
  A type that describes why the system permanently invalidated a tip.
### Structures
- [struct Event](tips/event.md)
  A repeatable user-defined action.
- [struct GroupBuilder](tips/groupbuilder.md)
- [struct MaxDisplayDuration](tips/maxdisplayduration.md)
  Specifies the maximum amount of time a tip is displayed before it is invalidated.
- [struct Parameter](tips/parameter.md)
  A type that monitors the state of its wrapped value to reevaluate any dependent tip rules when the value changes.
- [struct Rule](tips/rule.md)
  A condition to meet before displaying a tip.
### Type Methods
- [static func configure([Tips.ConfigurationOption]) throws](tips/configure(_:).md)
  Loads and configures the persistent state of all tips in your app.
- [static func hideAllTipsForTesting()](tips/hidealltipsfortesting.md)
  Hide all tips regardless of their display rule eligibility for UI testing without tips.
- [static func hideTipsForTesting([any Tip.Type])](tips/hidetipsfortesting(_:).md)
  Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.
- [static func resetDatastore() throws](tips/resetdatastore.md)
  Resets the tips’ datastore to the initial state for re-testing tip display rules and eligibility.
- [static func showAllTipsForTesting()](tips/showalltipsfortesting.md)
  Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.
- [static func showTipsForTesting([any Tip.Type])](tips/showtipsfortesting(_:).md)
  Show specified tips regardless of their display rule eligibility or display frequency status for UI testing of certain tips.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips)*