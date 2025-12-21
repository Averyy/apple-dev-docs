# NSCoding

**Framework**: Foundation  
**Kind**: protocol

A protocol that enables an object to be encoded and decoded for archiving and distribution.

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
protocol NSCoding
```

#### Overview

The `NSCoding` protocol declares the two methods that a class must implement so that instances of that class can be encoded and decoded. This capability provides the basis for archiving (where objects and other structures are stored on disk) and distribution (where objects are copied to different address spaces).

In keeping with object-oriented design principles, an object being encoded or decoded is responsible for encoding and decoding its instance variables. A coder instructs the object to do so by invoking [`encode(with:)`](nscoding/encode(with:).md) or [`init(coder:)`](nscoding/init(coder:).md). [`encode(with:)`](nscoding/encode(with:).md) instructs the object to encode its instance variables to the coder provided; an object can receive this method any number of times. [`init(coder:)`](nscoding/init(coder:).md) instructs the object to initialize itself from data in the coder provided; as such, it replaces any other initialization method and is sent only once per object. Any object class that should be codeable must adopt the `NSCoding` protocol and implement its methods.

It is important to consider the possible types of archiving that a coder supports. In macOS 10.2 and later, keyed archiving is preferred. You may, however, need to support classic archiving. For details, see [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Topics

### Initializing with a coder
- [init?(coder: NSCoder)](nscoding/init(coder:).md)
### Encoding with a coder
- [func encode(with: NSCoder)](nscoding/encode(with:).md)
  Encodes the receiver using a given archiver.

## Relationships

### Inherited By
- [NSSecureCoding](nssecurecoding.md)
### Conforming Types
- [ByteCountFormatter](bytecountformatter.md)
- [CachedURLResponse](cachedurlresponse.md)
- [DateComponentsFormatter](datecomponentsformatter.md)
- [DateFormatter](dateformatter.md)
- [DateIntervalFormatter](dateintervalformatter.md)
- [Dimension](dimension.md)
- [EnergyFormatter](energyformatter.md)
- [FileHandle](filehandle.md)
- [FileWrapper](filewrapper.md)
- [Formatter](formatter.md)
- [HTTPURLResponse](httpurlresponse.md)
- [ISO8601DateFormatter](iso8601dateformatter.md)
- [LengthFormatter](lengthformatter.md)
- [ListFormatter](listformatter.md)
- [MassFormatter](massformatter.md)
- [MeasurementFormatter](measurementformatter.md)
- [MessagePort](messageport.md)
- [NSAffineTransform](nsaffinetransform.md)
- [NSAppleEventDescriptor](nsappleeventdescriptor.md)
- [NSArray](nsarray.md)
- [NSAttributedString](nsattributedstring.md)
- [NSCalendar](nscalendar.md)
- [NSCharacterSet](nscharacterset.md)
- [NSCloneCommand](nsclonecommand.md)
- [NSCloseCommand](nsclosecommand.md)
- [NSComparisonPredicate](nscomparisonpredicate.md)
- [NSCompoundPredicate](nscompoundpredicate.md)
- [NSCountCommand](nscountcommand.md)
- [NSCountedSet](nscountedset.md)
- [NSCreateCommand](nscreatecommand.md)
- [NSData](nsdata.md)
- [NSDataDetector](nsdatadetector.md)
- [NSDate](nsdate.md)
- [NSDateComponents](nsdatecomponents.md)
- [NSDateInterval](nsdateinterval.md)
- [NSDecimalNumber](nsdecimalnumber.md)
- [NSDecimalNumberHandler](nsdecimalnumberhandler.md)
- [NSDeleteCommand](nsdeletecommand.md)
- [NSDictionary](nsdictionary.md)
- [NSError](nserror.md)
- [NSException](nsexception.md)
- [NSExistsCommand](nsexistscommand.md)
- [NSExpression](nsexpression.md)
- [NSExtensionItem](nsextensionitem.md)
- [NSFileSecurity](nsfilesecurity.md)
- [NSGetCommand](nsgetcommand.md)
- [NSHashTable](nshashtable.md)
- [NSIndexPath](nsindexpath.md)
- [NSIndexSet](nsindexset.md)
- [NSIndexSpecifier](nsindexspecifier.md)
- [NSLocale](nslocale.md)
- [NSLogicalTest](nslogicaltest.md)
- [NSMachPort](nsmachport.md)
- [NSMapTable](nsmaptable.md)
- [NSMeasurement](nsmeasurement.md)
- [NSMiddleSpecifier](nsmiddlespecifier.md)
- [NSMoveCommand](nsmovecommand.md)
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
- [NSNameSpecifier](nsnamespecifier.md)
- [NSNotification](nsnotification.md)
- [NSNull](nsnull.md)
- [NSNumber](nsnumber.md)
- [NSOrderedSet](nsorderedset.md)
- [NSOrthography](nsorthography.md)
- [NSPersonNameComponents](nspersonnamecomponents.md)
- [NSPointerArray](nspointerarray.md)
- [NSPredicate](nspredicate.md)
- [NSPropertySpecifier](nspropertyspecifier.md)
- [NSPurgeableData](nspurgeabledata.md)
- [NSQuitCommand](nsquitcommand.md)
- [NSRandomSpecifier](nsrandomspecifier.md)
- [NSRangeSpecifier](nsrangespecifier.md)
- [NSRegularExpression](nsregularexpression.md)
- [NSRelativeSpecifier](nsrelativespecifier.md)
- [NSScriptCommand](nsscriptcommand.md)
- [NSScriptCommandDescription](nsscriptcommanddescription.md)
- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
- [NSScriptWhoseTest](nsscriptwhosetest.md)
- [NSSet](nsset.md)
- [NSSetCommand](nssetcommand.md)
- [NSSortDescriptor](nssortdescriptor.md)
- [NSSpecifierTest](nsspecifiertest.md)
- [NSString](nsstring.md)
- [NSTextCheckingResult](nstextcheckingresult.md)
- [NSTimeZone](nstimezone.md)
- [NSURL](nsurl.md)
- [NSURLQueryItem](nsurlqueryitem.md)
- [NSURLRequest](nsurlrequest.md)
- [NSUUID](nsuuid.md)
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md)
- [NSValue](nsvalue.md)
- [NSWhoseSpecifier](nswhosespecifier.md)
- [NSXPCListenerEndpoint](nsxpclistenerendpoint.md)
- [NumberFormatter](numberformatter.md)
- [PersonNameComponentsFormatter](personnamecomponentsformatter.md)
- [Port](port.md)
- [RelativeDateTimeFormatter](relativedatetimeformatter.md)
- [SocketPort](socketport.md)
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
- [UnitEnergy.EnergyKit](unitenergy/energykit.md)
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
- [typealias Codable](../Swift/Codable.md)
  A type that can convert itself into and out of an external representation.
- [protocol NSSecureCoding](nssecurecoding.md)
  A protocol that enables encoding and decoding in a manner that is robust against object substitution attacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoding)*