# Audio routing

**Framework**: AVFAudio

Inspect and configure audio routes, ports, and data sources.

## Topics

### Inspecting the current route
- [var currentRoute: AVAudioSessionRouteDescription](avaudiosession/currentroute.md)
  A description of the current audio route’s input and output ports.
- [class AVAudioSessionRouteDescription](avaudiosessionroutedescription.md)
  An object that describes the input and output ports associated with a session’s audio route.
- [class AVAudioSessionPortDescription](avaudiosessionportdescription.md)
  Information about the capabilities of the port and the hardware channels it supports.
- [class let routeChangeNotification: NSNotification.Name](avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.
### Configuring inputs
- [var isInputAvailable: Bool](avaudiosession/isinputavailable.md)
  A Boolean value that indicates whether an audio input path is available.
- [var availableInputs: [AVAudioSessionPortDescription]?](avaudiosession/availableinputs.md)
  An array of input ports available for audio routing.
- [var preferredInput: AVAudioSessionPortDescription?](avaudiosession/preferredinput.md)
  The preferred input port for audio routing.
- [func setPreferredInput(AVAudioSessionPortDescription?) throws](avaudiosession/setpreferredinput(_:).md)
  Sets the preferred input port for audio routing.
- [var inputDataSource: AVAudioSessionDataSourceDescription?](avaudiosession/inputdatasource.md)
  The currently selected input data source.
- [var inputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/inputdatasources.md)
  An array of available data sources for the audio session’s current input port.
- [func setInputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setinputdatasource(_:).md)
  Selects a data source for the audio session’s current input port.
- [class let availableInputsChangeNotification: NSNotification.Name](avaudiosession/availableinputschangenotification.md)
### Configuring outputs
- [var outputDataSources: [AVAudioSessionDataSourceDescription]?](avaudiosession/outputdatasources.md)
  An array of available output data sources for the current audio route.
- [var outputDataSource: AVAudioSessionDataSourceDescription?](avaudiosession/outputdatasource.md)
  The currently selected output data source.
- [func setOutputDataSource(AVAudioSessionDataSourceDescription?) throws](avaudiosession/setoutputdatasource(_:).md)
  Sets the output data source for an audio session.
- [class AVAudioSessionDataSourceDescription](avaudiosessiondatasourcedescription.md)
  An object that defines a data source for an audio input or output, giving information such as the source’s name, location, and orientation.
- [func overrideOutputAudioPort(AVAudioSession.PortOverride) throws](avaudiosession/overrideoutputaudioport(_:).md)
  Temporarily changes the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/audio-routing)*