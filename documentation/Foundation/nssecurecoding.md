# NSSecureCoding

**Framework**: Foundation  
**Kind**: protocol

A protocol that enables encoding and decoding in a manner that is robust against object substitution attacks.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSSecureCoding : NSCoding
```

#### Overview

Historically, many classes decoded instances of themselves like this:

This technique is potentially unsafe because by the time you can verify the class type, the object has already been constructed, and if this is part of a collection class, potentially inserted into an object graph.

In order to conform to [`NSSecureCoding`](nssecurecoding.md):

- An object that does not override [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) can conform to `NSSecureCoding` without any changes (assuming that it is a subclass of another class that conforms).
- An object that does override [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) must decode any enclosed objects using the [`decodeObjectOfClass:forKey:`](nscoder/decodeobjectofclass:forkey:.md) method. For example:

In addition, the class must override the getter for its [`supportsSecureCoding`](nssecurecoding/supportssecurecoding.md) property to return [`true`](https://developer.apple.com/documentation/swift/true).

For more information about how this relates to the NSXPC API, see [`Creating XPC Services`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingXPCServices.html#//apple_ref/doc/uid/10000172i-SW6) in [`Daemons and Services Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i).

## Topics

### Checking for Secure Coding
- [static var supportsSecureCoding: Bool](nssecurecoding/supportssecurecoding.md)
  A Boolean value that indicates whether or not the class supports secure coding.

## Relationships

### Inherits From
- [NSCoding](nscoding.md)
### Conforming Types
- [CachedURLResponse](cachedurlresponse.md)
- [Dimension](dimension.md)
- [FileHandle](filehandle.md)
- [FileWrapper](filewrapper.md)
- [HTTPURLResponse](httpurlresponse.md)
- [ISO8601DateFormatter](iso8601dateformatter.md)
- [MeasurementFormatter](measurementformatter.md)
- [NSAffineTransform](nsaffinetransform.md)
- [NSAppleEventDescriptor](nsappleeventdescriptor.md)
- [NSArray](nsarray.md)
- [NSAttributedString](nsattributedstring.md)
- [NSCalendar](nscalendar.md)
- [NSCharacterSet](nscharacterset.md)
- [NSComparisonPredicate](nscomparisonpredicate.md)
- [NSCompoundPredicate](nscompoundpredicate.md)
- [NSCountedSet](nscountedset.md)
- [NSData](nsdata.md)
- [NSDataDetector](nsdatadetector.md)
- [NSDate](nsdate.md)
- [NSDateComponents](nsdatecomponents.md)
- [NSDateInterval](nsdateinterval.md)
- [NSDecimalNumber](nsdecimalnumber.md)
- [NSDictionary](nsdictionary.md)
- [NSError](nserror.md)
- [NSException](nsexception.md)
- [NSExpression](nsexpression.md)
- [NSExtensionItem](nsextensionitem.md)
- [NSFileSecurity](nsfilesecurity.md)
- [NSHashTable](nshashtable.md)
- [NSIndexPath](nsindexpath.md)
- [NSIndexSet](nsindexset.md)
- [NSLocale](nslocale.md)
- [NSMapTable](nsmaptable.md)
- [NSMeasurement](nsmeasurement.md)
- [NSMutableArray](nsmutablearray.md)
- [NSMutableAttributedString](nsmutableattributedstring.md)
- [NSMutableCharacterSet](nsmutablecharacterset.md)
- [NSMutableData](nsmutabledata.md)
- [NSMutableDictionary](nsmutabledictionary.md)
- [NSMutableIndexSet](nsmutableindexset.md)
- [NSMutableOrderedSet](nsmutableorderedset.md)
- [NSMutableSet](nsmutableset.md)
- [NSMutableString](nsmutablestring.md)
- [NSMutableURLRequest](nsmutableurlrequest.md)
- [NSNull](nsnull.md)
- [NSNumber](nsnumber.md)
- [NSOrderedSet](nsorderedset.md)
- [NSOrthography](nsorthography.md)
- [NSPersonNameComponents](nspersonnamecomponents.md)
- [NSPointerArray](nspointerarray.md)
- [NSPredicate](nspredicate.md)
- [NSPurgeableData](nspurgeabledata.md)
- [NSRegularExpression](nsregularexpression.md)
- [NSSet](nsset.md)
- [NSSortDescriptor](nssortdescriptor.md)
- [NSString](nsstring.md)
- [NSTextCheckingResult](nstextcheckingresult.md)
- [NSTimeZone](nstimezone.md)
- [NSURL](nsurl.md)
- [NSURLQueryItem](nsurlqueryitem.md)
- [NSURLRequest](nsurlrequest.md)
- [NSUUID](nsuuid.md)
- [NSValue](nsvalue.md)
- [NSXPCListenerEndpoint](nsxpclistenerendpoint.md)
- [URLAuthenticationChallenge](urlauthenticationchallenge.md)
- [URLCredential](urlcredential.md)
- [URLProtectionSpace](urlprotectionspace.md)
- [URLResponse](urlresponse.md)
- [Unit](unit.md)
- [UnitAcceleration](unitacceleration.md)
- [UnitAngle](unitangle.md)
- [UnitArea](unitarea.md)
- [UnitConcentrationMass](unitconcentrationmass.md)
- [UnitConverterLinear](unitconverterlinear.md)
- [UnitDispersion](unitdispersion.md)
- [UnitDuration](unitduration.md)
- [UnitElectricCharge](unitelectriccharge.md)
- [UnitElectricCurrent](unitelectriccurrent.md)
- [UnitElectricPotentialDifference](unitelectricpotentialdifference.md)
- [UnitElectricResistance](unitelectricresistance.md)
- [UnitEnergy](unitenergy.md)
- [UnitFrequency](unitfrequency.md)
- [UnitFuelEfficiency](unitfuelefficiency.md)
- [UnitIlluminance](unitilluminance.md)
- [UnitInformationStorage](unitinformationstorage.md)
- [UnitLength](unitlength.md)
- [UnitMass](unitmass.md)
- [UnitPower](unitpower.md)
- [UnitPressure](unitpressure.md)
- [UnitSpeed](unitspeed.md)
- [UnitTemperature](unittemperature.md)
- [UnitVolume](unitvolume.md)

## See Also

- [Encoding and Decoding Custom Types](encoding-and-decoding-custom-types.md)
  Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [typealias Codable = Decodable & Encodable](../Swift/Codable.md)
  A type that can convert itself into and out of an external representation.
- [protocol NSCoding](nscoding.md)
  A protocol that enables an object to be encoded and decoded for archiving and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssecurecoding)*