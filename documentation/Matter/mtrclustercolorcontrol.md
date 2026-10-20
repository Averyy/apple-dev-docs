# MTRClusterColorControl

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterColorControl
```

```objc
@interface MTRClusterColorControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustercolorcontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustercolorcontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func colorLoopSet(with: MTRColorControlClusterColorLoopSetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/colorloopset%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func colorLoopSet(with: MTRColorControlClusterColorLoopSetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/colorloopset%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func enhancedMoveHue(with: MTRColorControlClusterEnhancedMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedmovehue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func enhancedMoveHue(with: MTRColorControlClusterEnhancedMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedmovehue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func enhancedMoveToHue(with: MTRColorControlClusterEnhancedMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedmovetohue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func enhancedMoveToHue(with: MTRColorControlClusterEnhancedMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedmovetohue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func enhancedMoveToHueAndSaturation(with: MTRColorControlClusterEnhancedMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedmovetohueandsaturation%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func enhancedMoveToHueAndSaturation(with: MTRColorControlClusterEnhancedMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedmovetohueandsaturation%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func enhancedStepHue(with: MTRColorControlClusterEnhancedStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedstephue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func enhancedStepHue(with: MTRColorControlClusterEnhancedStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/enhancedstephue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveColor(with: MTRColorControlClusterMoveColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movecolor%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveColor(with: MTRColorControlClusterMoveColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movecolor%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveColorTemperature(with: MTRColorControlClusterMoveColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movecolortemperature%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveColorTemperature(with: MTRColorControlClusterMoveColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movecolortemperature%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveHue(with: MTRColorControlClusterMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movehue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveHue(with: MTRColorControlClusterMoveHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movehue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveSaturation(with: MTRColorControlClusterMoveSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movesaturation%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveSaturation(with: MTRColorControlClusterMoveSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movesaturation%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToColor(with: MTRColorControlClusterMoveToColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetocolor%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToColor(with: MTRColorControlClusterMoveToColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetocolor%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToColorTemperature(with: MTRColorControlClusterMoveToColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetocolortemperature%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToColorTemperature(with: MTRColorControlClusterMoveToColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetocolortemperature%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToHue(with: MTRColorControlClusterMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetohue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToHue(with: MTRColorControlClusterMoveToHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetohue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToHueAndSaturation(with: MTRColorControlClusterMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetohueandsaturation%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToHueAndSaturation(with: MTRColorControlClusterMoveToHueAndSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetohueandsaturation%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func moveToSaturation(with: MTRColorControlClusterMoveToSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetosaturation%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func moveToSaturation(with: MTRColorControlClusterMoveToSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/movetosaturation%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeColorCapabilities(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorcapabilities%28with%29.md)
- [func readAttributeColorLoopActive(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorloopactive%28with%29.md)
- [func readAttributeColorLoopDirection(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorloopdirection%28with%29.md)
- [func readAttributeColorLoopStartEnhancedHue(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorloopstartenhancedhue%28with%29.md)
- [func readAttributeColorLoopStoredEnhancedHue(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorloopstoredenhancedhue%28with%29.md)
- [func readAttributeColorLoopTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorlooptime%28with%29.md)
- [func readAttributeColorMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolormode%28with%29.md)
- [func readAttributeColorPointBIntensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointbintensity%28with%29.md)
- [func readAttributeColorPointBX(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointbx%28with%29.md)
- [func readAttributeColorPointBY(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointby%28with%29.md)
- [func readAttributeColorPointGIntensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointgintensity%28with%29.md)
- [func readAttributeColorPointGX(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointgx%28with%29.md)
- [func readAttributeColorPointGY(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointgy%28with%29.md)
- [func readAttributeColorPointRIntensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointrintensity%28with%29.md)
- [func readAttributeColorPointRX(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointrx%28with%29.md)
- [func readAttributeColorPointRY(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolorpointry%28with%29.md)
- [func readAttributeColorTempPhysicalMaxMireds(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolortempphysicalmaxmireds%28with%29.md)
- [func readAttributeColorTempPhysicalMinMireds(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolortempphysicalminmireds%28with%29.md)
- [func readAttributeColorTemperatureMireds(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecolortemperaturemireds%28with%29.md)
- [func readAttributeCompensationText(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecompensationtext%28with%29.md)
- [func readAttributeCoupleColorTempToLevelMinMireds(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecouplecolortemptolevelminmireds%28with%29.md)
- [func readAttributeCurrentHue(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecurrenthue%28with%29.md)
- [func readAttributeCurrentSaturation(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecurrentsaturation%28with%29.md)
- [func readAttributeCurrentX(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecurrentx%28with%29.md)
- [func readAttributeCurrentY(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributecurrenty%28with%29.md)
- [func readAttributeDriftCompensation(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributedriftcompensation%28with%29.md)
- [func readAttributeEnhancedColorMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeenhancedcolormode%28with%29.md)
- [func readAttributeEnhancedCurrentHue(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeenhancedcurrenthue%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeNumberOfPrimaries(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributenumberofprimaries%28with%29.md)
- [func readAttributeOptions(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeoptions%28with%29.md)
- [func readAttributePrimary1Intensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary1intensity%28with%29.md)
- [func readAttributePrimary1X(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary1x%28with%29.md)
- [func readAttributePrimary1Y(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary1y%28with%29.md)
- [func readAttributePrimary2Intensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary2intensity%28with%29.md)
- [func readAttributePrimary2X(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary2x%28with%29.md)
- [func readAttributePrimary2Y(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary2y%28with%29.md)
- [func readAttributePrimary3Intensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary3intensity%28with%29.md)
- [func readAttributePrimary3X(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary3x%28with%29.md)
- [func readAttributePrimary3Y(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary3y%28with%29.md)
- [func readAttributePrimary4Intensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary4intensity%28with%29.md)
- [func readAttributePrimary4X(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary4x%28with%29.md)
- [func readAttributePrimary4Y(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary4y%28with%29.md)
- [func readAttributePrimary5Intensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary5intensity%28with%29.md)
- [func readAttributePrimary5X(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary5x%28with%29.md)
- [func readAttributePrimary5Y(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary5y%28with%29.md)
- [func readAttributePrimary6Intensity(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary6intensity%28with%29.md)
- [func readAttributePrimary6X(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary6x%28with%29.md)
- [func readAttributePrimary6Y(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeprimary6y%28with%29.md)
- [func readAttributeRemainingTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributeremainingtime%28with%29.md)
- [func readAttributeStartUpColorTemperatureMireds(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributestartupcolortemperaturemireds%28with%29.md)
- [func readAttributeWhitePointX(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributewhitepointx%28with%29.md)
- [func readAttributeWhitePointY(with: MTRReadParams?) -> [String : Any]?](./mtrclustercolorcontrol/readattributewhitepointy%28with%29.md)
- [func stepColor(with: MTRColorControlClusterStepColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stepcolor%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stepColor(with: MTRColorControlClusterStepColorParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stepcolor%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stepColorTemperature(with: MTRColorControlClusterStepColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stepcolortemperature%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stepColorTemperature(with: MTRColorControlClusterStepColorTemperatureParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stepcolortemperature%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stepHue(with: MTRColorControlClusterStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stephue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stepHue(with: MTRColorControlClusterStepHueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stephue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stepSaturation(with: MTRColorControlClusterStepSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stepsaturation%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stepSaturation(with: MTRColorControlClusterStepSaturationParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stepsaturation%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stopMoveStep(with: MTRColorControlClusterStopMoveStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stopmovestep%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stopMoveStep(with: MTRColorControlClusterStopMoveStepParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustercolorcontrol/stopmovestep%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeColorPointBIntensity(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointbintensity%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointBIntensity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointbintensity%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointBX(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointbx%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointBX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointbx%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointBY(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointby%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointBY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointby%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointGIntensity(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointgintensity%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointGIntensity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointgintensity%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointGX(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointgx%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointGX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointgx%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointGY(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointgy%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointGY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointgy%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointRIntensity(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointrintensity%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointRIntensity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointrintensity%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointRX(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointrx%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointRX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointrx%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeColorPointRY(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributecolorpointry%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeColorPointRY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributecolorpointry%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributeoptions%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOptions(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributeoptions%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeStartUpColorTemperatureMireds(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributestartupcolortemperaturemireds%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeStartUpColorTemperatureMireds(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributestartupcolortemperaturemireds%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeWhitePointX(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributewhitepointx%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeWhitePointX(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributewhitepointx%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeWhitePointY(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustercolorcontrol/writeattributewhitepointy%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeWhitePointY(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustercolorcontrol/writeattributewhitepointy%28withvalue,expectedvalueinterval,params%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercolorcontrol)*